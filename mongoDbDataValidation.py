from pymongo.errors import InvalidDocument


webAppSchema = {

    "type" : "object",
        "properties" : {
            "user" : {
                "type" : "string"
            },
            "title" : {
                "type" : "string"
            },
            "content" : {
                "type" : "string"
            }
        },
    "required" : ["user","title","content"]
}


def validateDocument(document):
    if document != None:
        if document.validate(document, schema=webAppSchema):
            return document
        else:
            raise InvalidDocument("Invalid Document")
    

