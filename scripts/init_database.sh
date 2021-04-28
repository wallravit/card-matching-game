SCRIPT_DIR=$(dirname "$0")
export PYTHONPATH="$SCRIPT_DIR/.."
python3 "$SCRIPT_DIR/../api/utils/init_db.py" $@