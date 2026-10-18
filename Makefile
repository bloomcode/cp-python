PY ?= python3

.PHONY: test progress

# make test            every exercise
# make test EX=3.2     one exercise
# make test EX=3       one chapter
test:
ifeq ($(EX),)
	$(PY) -m pytest -q
else
	@ex="$(EX)"; case "$$ex" in *.*) ch="$${ex%.*}" ;; *) ch="$$ex" ;; esac; tag=$$(printf '%02d' $$ch); \
	f=$$(ls tests/test_ch$${tag}_*.py); \
	case "$$ex" in \
	  *.*) $(PY) -m pytest -q "$$f::test_ex_$$(echo "$$ex" | tr . _)" ;; \
	  *) $(PY) -m pytest -q "$$f" ;; \
	esac
endif

progress:
	$(PY) tools/progress.py
