from pages.js_dialogs_page import JsDialogsPage


def test_js_alert_accept(page):
    dialogs_page = JsDialogsPage(page)
    dialogs_page.load()

    def handle_dialog(dialog):
        assert dialog.type == "alert"
        assert "I am a Js Alert" in dialog.message
        dialog.accept()

    page.on("dialog", handle_dialog)
    dialogs_page.trigger_alert()
    dialogs_page.verify_response_contains("OK")


def test_js_confirm_dismiss(page):
    dialogs_page = JsDialogsPage(page)
    dialogs_page.load()

    def handle_dialog(dialog):
        assert dialog.type == "confirm"
        dialog.dismiss()

    page.on("dialog", handle_dialog)
    dialogs_page.trigger_confirm()
    dialogs_page.verify_response_contains("Cancel")


def test_js_prompt_accept_with_text(page):
    dialogs_page = JsDialogsPage(page)
    dialogs_page.load()

    def handle_dialog(dialog):
        assert dialog.type == "prompt"
        dialog.accept("Jay test input")

    page.on("dialog", handle_dialog)
    dialogs_page.trigger_prompt()
    dialogs_page.verify_response_contains("Jay test input")
