from requests import get
from bs4 import BeautifulSoup



def remoteok_jobs(keyword):
    base_url = "https://remoteok.com/"
    search_term = f"remote-{keyword}-jobs"
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    response = get(f"{base_url}{search_term}", headers = headers)

    if response.status_code != 200:
        print("Can't request")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        result = []
        table = soup.find('table')
        table_body=table.find('tbody')

        rows = table.find_all('tr', class_="job")
        for row in rows:
            cols = row.find_all('td')
            for col in cols:
                company = col.find('h3')
                job_title = col.find('h2')
                infos = col.find_all('div', class_='location')
                link = col.find('a' , class_="preventLink")
                if company != None and job_title != None:
                    info = [ele.string for ele in infos]
                    job_data = {
                        'link': f"https://remoteok.com{link['href']}",
                        'company':company.string.strip('\n'),
                        'info':info,
                        'position':job_title.string.strip('\n')
                    }
                    result.append(job_data)
        return result
            
   