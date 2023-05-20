# My-TikTok-API
This TikTok Data API allows you to retrieve user information and video data from TikTok by providing the username

we define a single endpoint /tiktok/<username> that accepts a TikTok username as a parameter. It retrieves the user information and video data for the provided username and returns a JSON response containing the data.

You can run this Flask application, and then you can make GET requests to ```http://localhost:5000/tiktok/<username>``` to get the TikTok data for a specific username.

Note: Make sure you have the Flask and requests libraries installed 
  ```pip install flask requests``` before running the code.
  
## Base URL
The base URL for accessing the API is:``` http://localhost:5000```
  
## Endpoints
Retrieves user information and video data for a given TikTok username.

* URL: ```/tiktok/<username>```
* Method: GET
* URL Parameters:
  * ```username``` (required): The TikTok username for which you want to retrieve data.
* Success Response:
  * Code: 200 OK
  * Content: JSON object containing user information and videos information.
* Error Response:
  * Code: 500 Internal Server Error
  * Content: JSON object with an error field containing the error message.
  
 ## Sample Request
  ```
  GET /tiktok/johndoe
```

  ## Sample Response
  ```
  {
  "User Information": {
    "Username": "johndoe",
    "Total Followers": "10000",
    "Total Following": "500",
    "Total Likes": "5000"
  },
  "Videos Information": [
    {
      "Video_title": "Funny Cat Video",
      "Views": "1000",
      "Likes": "100",
      "Link": "/video/123456"
    },
    {
      "Video_title": "Dancing Challenge",
      "Views": "2000",
      "Likes": "150",
      "Link": "/video/789012"
    }
  ]
}
```
  
## Error Handling
In case of any errors, the API will return a JSON response with an ```error``` field containing the error message. The HTTP status code will be 500 Internal Server Error.

## Rate Limiting
The API does not currently impose any rate limits. However, please use the API responsibly and avoid making excessive requests.
