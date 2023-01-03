from django.http import HttpResponse


class StripeWH_Handler():
    """Handle stripe wh"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle unknown or unexpected wh events"""
        return HttpResponse(
            content=f'Unhandled WH received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle payment succeeded wh events"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle payment succeeded wh events"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
