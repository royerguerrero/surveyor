CURRENT_PATH=$PWD 

echo "🚀 Starting bot execution routine"
cd ~/Dev/surveyor

echo "🔥 Active virtual enviroment"
source ./.env/bin/activate

echo "📇 Expose Credentials"
source ./credentials.sh

echo "🤖 Bot deployed..."
python3 main.py

echo "🔫 The bot has finished the job"
echo "💣 Self-destruction in 3, 2, 1 ... 💥"
deactivate

cd $CURRENT_PATH
