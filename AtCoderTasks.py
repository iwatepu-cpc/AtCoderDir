from urllib.parse import urlparse
import requests
import bs4

__atcoder__ = 'https://atcoder.jp'

def get_task_urls(base_url):
    url = base_url+'/tasks'
    q = requests.get(url)
    if q.status_code != requests.codes.ok:
        print("Old system")
        url = base_url+'/assignments'
        q = requests.get(url)
        html = bs4.BeautifulSoup(q.text, 'html.parser')
        links = html.select('td.center > a')
    else:
        html = bs4.BeautifulSoup(q.text, 'html.parser')
        links = html.select('td.text-center > a')
    parsed = urlparse(url)
    return {l.text:'{uri.scheme}://{uri.netloc}'.format(uri=parsed)+l.attrs['href'] for l in links}

def get_samples(url):
    print("Fetch "+url)
    q = requests.get(url)
    html = bs4.BeautifulSoup(q.text, 'html.parser')
    samples = []
    for i in range(1, 30):
        isample = html.find(string='入力例 '+str(i))
        if isample is None:
            isample = html.find(string='入力例'+str(i))
            if isample is None:
                break
        osample = html.find(string='出力例 '+str(i))
        if osample is None:
            osample = html.find(string='出力例'+str(i))
            if osample is None:
                break
        print('Found '+str(i))
        #samples.append((isample.parent.next_sibling.text.replace('\r', ''), osample.parent.next_sibling.text.replace('\r', '')))
        samples.append((isample.parent.parent.find('pre').text.replace('\r', ''), osample.parent.parent.find('pre').text.replace('\r', '')))
    return samples
