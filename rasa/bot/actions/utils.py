# if the confidence of detected entity or entity role is lower than the threshold,
# let's consider that the entity is not detected
# at the moment, Rasa allows to set threshold in its pipeline for intent detection only,
# so let's have our own logic for entities
ENTITY_CONFIDENCE_THRESHOLD = 0.7
ROLE_CONFIDENCE_THRESHOLD = 0.7

# TODO: add unit tests for this function
def find_entity(entities, name: str, role: str = None):
    found_entity = None
    for entity in entities:
        if (
            entity["entity"] == name
            and entity.get("confidence_entity", -1) >= ENTITY_CONFIDENCE_THRESHOLD
            and (
                role == None
                or entity.get("role") == role
                and entity.get("confidence_role", -1) >= ROLE_CONFIDENCE_THRESHOLD
            )
        ):
            found_entity = entity
            break

    return found_entity
