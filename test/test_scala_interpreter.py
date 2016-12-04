import pytest

from metakernel_scalaspark.scala_kernel import initialize_scala_kernel


@pytest.fixture(scope="module")
def scala_kernel(request):
    wrapper = initialize_scala_kernel()
    return wrapper


def test_simple_expression(scala_kernel):
    result = scala_kernel.interpret("4 + 4")
    assert result == 'res0: Int = 8\n'


def test_completion(scala_kernel):
    scala_kernel.interpret("val x = 4")
    code = "x.toL"
    result = scala_kernel.complete(code, len(code))
    assert result == ['toLong']


# def test_interpreter_help(scala_kernel):
#     scala_kernel.interpret("val z = 5")
#     print(scala_kernel.jiloop.getClass().toString())
#     print(dir(scala_kernel.iMainOps))
#     scala_kernel.interpret("case class Foo(bar: String)")
#     h = scala_kernel.iMainOps.implicitsCommand("")
#     assert h == ''


def test_help(scala_kernel):
    scala_kernel.interpret("val x = 4")
    h = scala_kernel.get_help_on("x")

    scala_kernel.interpret("case class Foo(bar: String)")
    scala_kernel.interpret('val y = Foo("something") ')

    h1 = scala_kernel.get_help_on("y")
    h2 = scala_kernel.get_help_on("y.bar")

    assert h == "Int"
    assert h1 == "Foo"
    assert h2 == "String"
#
# print(wrapper.interpret("4 + 4"))
# print(wrapper.interpret("val x = 4"))
# print(wrapper.complete('x.toL', 5))
# print(wrapper.interpret("x * 2"))




# wrapper = initialize_scala_kernel()
#
# print(wrapper.interpret("4 + 4"))
# print(wrapper.interpret("val x = 4"))
# print(wrapper.complete('x.toL', 5))
# print(wrapper.interpret("x * 2"))