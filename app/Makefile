# 変数定義
MYPY = mypy
MYPY_CONFIG = mypy.ini
RUFF = ruff
SOURCE_DIR = .

# デフォルトのターゲット
.PHONY: all
all: check-types check-format lint

# 型チェック
.PHONY: check-types
check-types:
	$(MYPY) $(SOURCE_DIR) --config-file $(MYPY_CONFIG)

# Ruffによるフォーマット
.PHONY: format
format:
	$(RUFF) format $(SOURCE_DIR)

# Ruffによるフォーマットチェック（変更を適用せずチェックのみ）
.PHONY: check-format
check-format:
	$(RUFF) format --check $(SOURCE_DIR)

# Ruffによるlint
.PHONY: lint
lint:
	$(RUFF) check $(SOURCE_DIR)

# フォーマットとlintの修正
.PHONY: fix
fix:
	$(RUFF) check --fix $(SOURCE_DIR)
	$(RUFF) format $(SOURCE_DIR)

# ヘルプコマンド
.PHONY: help
help:
	@echo "Usage:"
	@echo "  make              - Run all checks (types, format, lint)"
	@echo "  make check-types  - Run mypy type checking"
	@echo "  make format       - Run ruff formatter"
	@echo "  make check-format - Check formatting without making changes"
	@echo "  make lint         - Run ruff linter"
	@echo "  make fix          - Auto-fix linting issues and format code"
	@echo "  make help         - Show this help message"

# デフォルトのターゲットを指定
.DEFAULT_GOAL := help