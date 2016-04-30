#!/bin/bash

INTERPRETER_NAME="wordlearner_bot_python3"
RUN_FILE_NAME="run_wordlearner_bot.sh"
MAIN_PY_FILE="main_languagelearner.py"

# Go to script's folder
cd `dirname $0`

mkdir databases

mkdir tokens
touch tokens/token

#create environment
virtualenv env
# install dependencies
env/bin/python3 env/bin/pip3 install -r requirements.txt
# create a better-named python interpreter link
ln -s env/bin/python3 ${INTERPRETER_NAME}

#create a run file
echo "#!/bin/bash

_term() {
echo "Caught termination signal!"
kill -TERM \"\$child\" 2>/dev/null
}

trap _term SIGTERM SIGINT

./${INTERPRETER_NAME} ${MAIN_PY_FILE} &

child=\$!
wait \"\$child\"

exit 0
" > $RUN_FILE_NAME

chmod +x $RUN_FILE_NAME

exit 0
