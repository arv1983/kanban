class ValidatorSignup:

    def signup_validator(self: dict):
        SIGNUP = ["name", "email", "password"]
        requered = [req for req in SIGNUP if req not in self]
        if requered:
            response = {
                "Erro": "Faltam campos obrigatórios",
                "recebido": [inf for inf in self],
                "faltantes": {
                    "Campos": requered,
                },
            },
            return response


