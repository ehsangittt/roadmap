`This is a documentation for shutting down and restarting servers in Aran.`
Using this Python code, you can turn off or restart your desired server from the region 
you select.
One important note is that you need to set your own API key in the .env file.
When creating the .env file, you also need to make some adjustments.
In your code you should add this 
``` 
from dotenv import load_dotenv

import os

load_dotenv() 

headers = {
    'Authorization': os.getenv("SECRET_KEY")
}

```
