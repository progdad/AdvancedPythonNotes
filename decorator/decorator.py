# 1. Define benchmark
def benchmark(iters):
    # 3. Define actual_decorator
    def actual_decorator(func):
        # 5. Define wrapper
        def wrapper(*args, **kwargs):
            # 8. Come into the loop
            for i in range(iters):
                return_value = func(*args, **kwargs)
            return return_value
        # 6. Return wrapper
        return wrapper

    # 4. Return actual_decorator
    return actual_decorator


# 2. Define fetch_webpage. Call benchmark function
@benchmark(iters=3)  # That's the same as: <benchmark(iters=3)(fetch_webpage)>
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


# 7. Create webpage variable and call wrapper
webpage = fetch_webpage('https://google.com')
