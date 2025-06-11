from ..alojamiento.models import LodgingResponse


def mapLodging(lodgings)->list[LodgingResponse]:
    lodgings = list(lodgings)
    for indice in range(len(lodgings)):
        lodgings[indice]["id"] = str(lodgings[indice]["_id"])
        lodgings[indice] = LodgingResponse(**lodgings[indice])

    return lodgings