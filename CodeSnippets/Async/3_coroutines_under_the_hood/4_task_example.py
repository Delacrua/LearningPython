import asyncio


def indent(count: int) -> str:
    return " " * (6 - (count * 3))


async def example(count: int) -> str:
    print(indent(count), "Before the first await")
    await asyncio.sleep(0)
    print(indent(count), "After the first await")
    if count == 0:
        print(indent(count), "Returning result")
        return "result"
    for i in range(count):
        print(indent(count), "Before await inside loop iteration", i)
        await asyncio.sleep(i)
        print(indent(count), "After await inside loop iteration", i)
    return await example(count - 1)


class TraceStep(asyncio.tasks._PyTask):
    def _Task__step(self, exc=None):
        print(f"<step name={self.get_name()} done={self.done()}>")
        result = super()._Task__step(exc=exc)
        print(f"<step name={self.get_name()} done={self.done()}>")



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_task_factory(lambda loop, coro: TraceStep(loop=loop, coro=coro))

    loop.run_until_complete(example(3))