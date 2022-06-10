class Validator:

    def base(requered: dict, data: dict):
        requered = [req for req in requered if req not in data]
        if requered:
            response = {
                "erro": "Faltam campos obrigatórios",
                "recebido": [inf for inf in data],
                "faltantes": {
                    "Campos": requered,
                },
            },
            return response      
  
    def signup_validator(data: dict):
        SIGNUP = ["name", "email", "password"]
        return Validator.base(SIGNUP, data)


    def login_validator(data: dict):
        LOGIN = ["email", "password"]
        return Validator.base(LOGIN, data)

    def group_create_validator(data: dict):
        GROUP = ["name"]
        return Validator.base(GROUP, data)



