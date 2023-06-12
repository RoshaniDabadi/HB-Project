from model import Health_Condition, db 


def create_Health_Condition(condition_name, condition_description, minCarbs, 
    maxCarbs, minCholesterol, maxCholesterol, minSaturatedFat,
    maxSaturatedFat, minSugar, maxSugar, minIron):

    condition = Health_Condition(
        condition_name=condition_name,
        condition_description=condition_description,
        min_carbs=minCarbs,
        max_carbs=maxCarbs,
        min_Cholesterol=minCholesterol,
        max_Cholesterol=maxCholesterol,
        min_SaturatedFat=minSaturatedFat,
        max_SaturatedFat=maxSaturatedFat,
        min_Sugar=minSugar,
        max_Sugar=maxSugar,
        min_Iron=minIron        
    )
    db.session.add(condition)
    db.session.commit()

    return condition


    #queryHealthCondition function -- to be added later
    #projectracker n movieratings lab exercises 