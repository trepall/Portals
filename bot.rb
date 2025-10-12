require 'telegram/bot'

token = '8129879226:AAGI-6i5iTcPBwaHltbBZn1zvXrzr2OMJF4'

Telegram::Bot::Client.run(token) do |bot|
  bot.listen do |message|
    if message.text == '/start'
      # Твое фото
      photo_url = "https://i.ibb.co/ZpTGYWC6/IMG-7434.jpg"
      
      # Кнопка "Открыть"
      keyboard = [
        [Telegram::Bot::Types::InlineKeyboardButton.new(text: 'Открыть в приложении', url: 'https://google.com')]
      ]
      markup = Telegram::Bot::Types::InlineKeyboardMarkup.new(inline_keyboard: keyboard)
      
      # Отправляем фото с текстом и кнопкой
      bot.api.send_photo(
        chat_id: message.chat.id,
        photo: photo_url,
        caption: "Welcome to Portals! Discover, trade, and collect unique digital gifts in our marketplace. Start exploring now!",
        reply_markup: markup
      )
    end
  end
end
