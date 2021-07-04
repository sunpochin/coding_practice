import React from 'react';

export default function Square({black}) {
  const fill = black ? 'black' : 'white';
  return <div style={{backgroundColor: fill}} />
}

