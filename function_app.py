import azure.functions as func
import logging
from bs4 import BeautifulSoup
from urllib.request import urlopen

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="findchips_search")
def findchips_search(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    part_number = req.params.get('part_number')
    if not part_number:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            part_number = req_body.get('part_number')

    if part_number:
        url="https://www.findchips.com/search/"
        page = urlopen(url+part_number)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find_all(class_='distributor-results')
        html_output = ""
        for result in results:
            html_output += str(result.contents[3])
        # filename = "chip.html"
        # with open(filename, "w", encoding="utf-8") as file:
        #     for result in results:
        #         file.write(str(result.contents[3]))
        #     file.close()
        return func.HttpResponse(html_output)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )