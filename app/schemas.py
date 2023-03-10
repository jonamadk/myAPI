
from pydantic import BaseModel

from pydantic import BaseModel, constr

class LineOfBusinessSchema(BaseModel):
    _id:str
    code:str
    carrierCode:str
    broadLineBusinessCode:str
    carrierName:str
    carrierWebsite:str
    enabled:str
    _class:str
    carrierLogo:str
    jurisdictions:str
    # integrationType:str
    # stateOrProvinceCode:str
    # stateOrProvinceName:str
    # integrationType:str
    # stateOrProvinceCode:str
    # stateOrProvinceName:str
    
    class Config:
        orm_mode = True


class UpdateLineOfBusinessSchema(LineOfBusinessBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False
        
        
    
    
