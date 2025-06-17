


class TestExample:
    def test_example(self,set_up_browsers):
        driver = set_up_browsers
        driver.get("https://skillbox.ru")
        assert "Skillbox" == driver.title

