from pydantic import BaseModel
from fastapi import Form
class feature_attributes(BaseModel):
    Temperature:int
    RH:int
    Ws:int
    Rain:float
    FFMC:float
    DMC:float
    ISI:float
    Classes:float
    Region:float



    @classmethod
    def as_form(
            cls,
            Temperature:int=Form(...),
            RH:int=Form(...),
            Ws:int=Form(...),
            Rain:float=Form(...),
            FFMC:float=Form(...),
            DMC:float=Form(...),
            ISI:float=Form(...),
            Classes:float=Form(...),
            Region:float=Form(...)

    ):
        return cls(
            Temperature=Temperature,
            RH=RH,
            Ws=Ws,
            Rain=Rain,
            FFMC=FFMC,
            DMC=DMC,
            ISI=ISI,
            Classes=Classes,
            Region=Region,
        )    
