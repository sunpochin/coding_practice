class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        hmap = {}
        def process(times: int, domain: str):
            while True:
                # print('domain: ', domain)
                hmap[domain] = times + hmap.get(domain, 0)
                
                idx = domain.find('.')
                if (-1 == idx):
                    break
                domain = domain[idx + 1:]
            
        print('cpdomains: ', cpdomains)
        for it in cpdomains:
            splitted = it.split(' ')
            # print(splitted)
            process(int(splitted[0]), splitted[1])
            
        # print('hmap: ', hmap)
        result = []
        for it in hmap:
            # print('it: ', it)
            tmp = str(hmap.get(it) ) + ' ' + it
            result.append(tmp)
        return result
            

            