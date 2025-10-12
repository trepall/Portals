require 'telegram/bot'

token = ENV['TELEGRAM_BOT_TOKEN']

puts "🚀 Starting bot with token: #{token[0..10]}..."

begin
  Telegram::Bot::Client.run(token) do |bot|
    bot.listen do |message|
      puts "Received message: #{message.text}"
      
      case message.text
      when '/start'
        caption = "Welcome to Portals! Discover, trade, and collect unique digital gifts in our marketplace. Start exploring now!"
        photo_url = "https://i.ibb.co/ZpTGYWC6/IMG-7434.jpg"
        
        keyboard = [
          [
            Telegram::Bot::Types::InlineKeyboardButton.new(
              text: 'Открыть в приложении',
              url: 'https://example.com'  # ⏳ ВРЕМЕННАЯ ССЫЛКА
            )
          ]
        ]
        
        markup = Telegram::Bot::Types::InlineKeyboardMarkup.new(inline_keyboard: keyboard)
        
        bot.api.send_photo(
          chat_id: message.chat.id,
          photo: photo_url,
          caption: caption,
          reply_markup: markup
        )
        
        puts "✅ Sent welcome message to #{message.chat.id}"
      end
    end
  end
rescue => e
  puts "❌ Bot error: #{e.message}"
  sleep(10)
  retry
end
