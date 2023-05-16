# profile script, sorting by total function time (excluding subcalls)
python -m cProfile -s time test_script_fct.py
# ...sorting by cumulative time (including subcalls)
python -m cProfile -s cumtime test_script_fct.py
# ...showing top 20 entries
python -m cProfile -s time test_script_fct.py | head -n20

# output to file
python -m cProfile -o test_script_fct.prof test_script_fct.py

# visualizing the output using snakeviz
snakeviz test_script_fct.py

# visualizing saved profiler output using command-line tool
python -m pstats test_script_fct.prof

# line-profiling a script
# (needs to use @profile or similar to tag functions to be profiled;
#  see https://github.com/pyutils/line_profiler)
kernprof -lv test_script_line.py
