<?php
$url = "https://scraper-api.smartproxy.com/v2/scrape";

$payload = json_encode([
    "target" => "amazon_search",
    "query" => "laptop",
    "page_from" => "1",
    "parse" => true,
]);

$headers = [
    "Accept: application/json",
    "Content-Type: application/json",
    "Authorization: Basic [your basic authentication token]"
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$response = curl_exec($ch);
if (curl_errno($ch)) {
    echo 'Error:' . curl_error($ch);
}
curl_close($ch);

echo $response;
?>