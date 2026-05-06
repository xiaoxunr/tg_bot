import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# 配置日志
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 机器人 Token（后面在 Render 里用环境变量填）
import os
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# /start 命令
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"👋 你好！我是你的机器人，已成功上线！\n你的ID：{update.effective_user.id}")

# /help 命令
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("📖 可用命令：\n/start - 开始\n/help - 帮助")

def main() -> None:
    if not BOT_TOKEN:
        logger.error("❌ 请设置 BOT_TOKEN 环境变量！")
        return

    # 初始化机器人
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # 注册命令处理器
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # 启动轮询模式（完美适配 Render Background Workers）
    updater.start_polling()
    logger.info("✅ 机器人已启动，正在运行...")
    updater.idle()

if __name__ == "__main__":
    main()
