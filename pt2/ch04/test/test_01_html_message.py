from typing import Callable, List, Protocol


class Message:
    header: str
    body: str
    footer: str


class Renderer(Protocol):
    def render(self, msg: Message):
        ...


class HeaderRenderer(Renderer):
    def render(self, msg: Message):
        return f"<h1>{msg.header}</h1>"


class BodyRenderer(Renderer):
    def render(self, msg: Message):
        return f"<b>{msg.body}</b>"


class FooterRenderer(Renderer):
    def render(self, msg: Message):
        return f"<i>{msg.footer}</i>"


class MessageRenderer(Renderer):
    sub_renderers: List[Callable] = [
        HeaderRenderer(),
        BodyRenderer(),
        FooterRenderer(),
    ]

    def render(self, msg: Message):
        # 결과를 계속 받아서 지속적으로 하나의 string에 aggregate
        output = (x.render(msg) for x in self.sub_renderers)
        result = "".join(output)

        return result


def test_message_renderer_uses_correct_sub_renderers():
    sut = MessageRenderer()

    renderers = sut.sub_renderers

    assert 3 == len(renderers)
    assert isinstance(renderers[0], HeaderRenderer)
    assert isinstance(renderers[1], BodyRenderer)
    assert isinstance(renderers[2], FooterRenderer)


def test_message_renderer_is_implemented_correctly(whole_code):
    import pathlib
    cwd = pathlib.Path().cwd() / "pt2/ch04/test/test_01_html_message.py"

    with open(cwd, "r", encoding="utf-8") as source_code:
        assert whole_code == source_code.read()


def test_rendering_a_message():
    sut = MessageRenderer()
    message: Message = Message()
    message.header = "h"
    message.body = "b"
    message.footer = "f"

    html = sut.render(message)

    assert "<h1>h</h1><b>b</b><i>f</i>" == html
