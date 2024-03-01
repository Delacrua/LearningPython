import asyncio

future = asyncio.Future()


if __name__ == "__main__":
    assert future.done() is False
    assert future.cancelled() is False
    try:
        future.result()
    except asyncio.exceptions.InvalidStateError as exc:
        assert "Result is not set" in str(exc)

    future.set_result("result")
    assert future.result() == "result"
    assert future.cancelled() is False
    assert future.done() is True
