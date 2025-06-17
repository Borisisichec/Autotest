# Указываем специальные цели, которые не являются именами файлов
.PHONY: run_tests show_cases


run_tests:
	echo "before test" && \
	conda activate skillbox_2 && \
	pytest && \
	echo "after test"

#show_cases:
#	echo "Collecting tests..." && \
#	conda activate skillbox_1 && \
#	pytest --collect-only
