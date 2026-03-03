from pydantic import BaseModel, EmailStr, field_validator, ValidationError

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    @classmethod
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value


try:
    user_data = {
        'name': 'Salah',
        'email': 'salah@gmail.com',
        'account_id': 12345
    }
    user = User(**user_data)
    print("User Created Successfully:")
    print(user.model_dump())
except ValidationError as e:
    print("Validation Error:", e.json())

print("-" * 30)

try:
    invalid_user = User(name="Ali", email="ali-wrong-email", account_id=-10)
except ValidationError as e:
    print("❌ Caught Expected Error:")
    print(e)