class Verbose:
    def __init__(self, *args):
        self.parents = args

    def __call__(self, *args, **kwargs):
        class Wrapper(*self.parents):
            def __init__(self, *args, **kwargs):
                super(Wrapper, self).__init__(*args, **kwargs)

            def vp(self, *args, **kwargs):
                if self.verbose:
                    print(*[f">>> {} - " + args[0]] + list(args[1:]), **kwargs)
