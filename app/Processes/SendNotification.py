import message_composer, message_sender, token_manager, app_manager

notification_definition = {
    "NotificationId" : "5524b041-e10e-4ed1-815f-271f52563fe2",
    "Type": "favorites",
    "Version": "1",
    "CatalogId": "489002",
    "SmallImageURL": "https://static0.tiendeo.com/upload_negocio/negocio_46/marker.png",
    "LargeImageURL": "https://static0.tiendeo.com/images/tiendas/399/catalogos/478051/paginas/med/00001.jpg",
    "IconURL" : "https://www.tiendeo.com/favicon.ico",
    "PromoCode": "promo-code",
    "Title": "texto a mostrar",
    "Body": "texto a mostrar",
    "CountryCode": "ES",
    "BaseStatsUrl": "https://tst.statsapi.tiendeo.com/",
    "DeepLink": "tiendeo://catalog/es/489002"
}

token = token_manager.search_token(user = 'victor.perez.berruezo@gmail.com')

app = app_manager.initialize_app()

android_message = message_composer.android_message(notification_definition)

message_sender.send_to_token(android_message, token, app)
