from pydantic import BaseModel,Field,conint,confloat
from fastapi import Form
class feature_attributes(BaseModel):
    Temperature:conint(ge=-50,le=60)
    RH:conint(ge=0,le=100)
    Ws:conint(ge=0,le=50)
    Rain:confloat(ge=0)
    FFMC:confloat(ge=0)
    DMC:confloat(ge=0)
    ISI:confloat(ge=0)
    Classes:conint(ge=0,le=1)
    Region:conint(ge=0,le=1)



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
            Classes:int=Form(...),
            Region:int=Form(...)

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
