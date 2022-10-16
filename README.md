# Setup

* Install dependencies from requirements.txt. for this, you can use - `pip install -r requirements.txt`.
* Create a *config.json* file with the following contentswith the following contents:

```json
 {
    "init" : {
        "token" : "your-api-token",
        "user_id" : 123456789 // your vk user_id
    },
    "preferences" : {
        "swear_words" : ["some", "swear", "words"],
        "censoring" : true // or false
    }
}
```

# Run

run *run.py* script

# Using

the bot provides the following functionsthe bot provides the following functions:

1. `/wiki <term>` - returns definition from wikipediareturns definition from wikipedia
2. `! <expression>`  - returns result of evaluated expression or error
3. censoring swear words from the list, example: `word => w**d`
