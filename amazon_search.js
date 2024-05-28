async function fetchAmazonData() {
    try {
        const response = await fetch("https://scraper-api.smartproxy.com/v2/scrape", {
            method: "POST",
            body: JSON.stringify({
                "target": "amazon_search",
                "query": "laptop",
                "page_from": "1",
                "parse": true
            }),
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Basic [your basic authentication token]"
            }
        });

        const data = await response.json();
        console.log(JSON.stringify(data));

    } catch (error) {
        console.log(error);
    }
}

fetchAmazonData();