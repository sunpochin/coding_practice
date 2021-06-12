import React, { useEffect, useState, useCallback } from "react";
import {
	BrowserRouter as Router,
	Route,
	Redirect,
	Switch,
} from "react-router-dom";

import Users from "./user/pages/Users";
import NewPlace from "./places/pages/NewPlace";
import UserPlaces from "./places/pages/UserPlaces";
import UpdatePlace from "./places/pages/UpdatePlace";
import Auth from "./user/pages/Auth";
import MainNavigation from "./shared/components/Navigation/MainNavigation";
import { AuthContext } from "./shared/context/auth-context";

let logoutTimer;

const App = () => {
	const [token, setToken] = useState(false);
  const [tokenExpirationDate, setTokenExpirationDate] = useState();
	const [userId, setUserId] = useState(false);

	const login = useCallback((uid, token, expirationDate) => {
		console.log("got token: ", token, ", uid: ", uid);
		setToken(token);
		setUserId(uid);
		const updatedExpiration =
			expirationDate || new Date(new Date().getTime() + 1000 * 60 * 60);
    setTokenExpirationDate(updatedExpiration);
		localStorage.setItem(
			"userData",
			JSON.stringify({
				userId: uid,
				token: token,
				expiration: updatedExpiration.toISOString(),
			})
		);
	}, []);

	const logout = useCallback(() => {
		setToken(null);
    setTokenExpirationDate(null);
		setUserId(null);
		localStorage.removeItem("userData");
	}, []);

  useEffect(() => {
    if (token && tokenExpirationDate) {
      const remainTime = tokenExpirationDate.getTime() - new Date().getTime();
      console.log('remainTime ', remainTime);
      logoutTimer = setTimeout(logout, remainTime);
    } else {
      console.log('useEffect logout ', token, tokenExpirationDate);
      // no token and no expirationDate, maybe 
      // 1. user manually logout.
      // 2. timeout called logout,
      clearTimeout(logoutTimer);
    };
  }, [token, logout, tokenExpirationDate])

	useEffect(() => {
		const storedData = JSON.parse(localStorage.getItem("userData"));
		if (
			storedData &&
			storedData.token &&
			new Date(storedData.expiration) > new Date()
		) {
			login(
				storedData.userId,
				storedData.token,
				new Date(storedData.expiration)
			);
		}
	}, [login]);

	let routes;
	if (token) {
		routes = (
			<Switch>
				<Route path="/" exact>
					<Users />
				</Route>
				<Route path="/:userId/places" exact>
					<UserPlaces />
				</Route>
				<Route path="/places/new" exact>
					<NewPlace />
				</Route>
				<Route path="/places/:placeId">
					<UpdatePlace />
				</Route>
				<Redirect to="/" />
			</Switch>
		);
	} else {
		routes = (
			<Switch>
				<Route path="/" exact>
					<Users />
				</Route>
				<Route path="/:userId/places" exact>
					<UserPlaces />
				</Route>
				<Route path="/auth">
					<Auth />
				</Route>
				<Redirect to="/auth" />
			</Switch>
		);
	}

	return (
		<AuthContext.Provider
			value={{
				isLoggedIn: !!token,
				token: token,
				userId: userId,
				login: login,
				logout: logout,
			}}
		>
			<Router>
				<MainNavigation />
				<main>{routes}</main>
			</Router>
		</AuthContext.Provider>
	);
};

export default App;
