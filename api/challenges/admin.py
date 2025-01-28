from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsxLexer
from .models import Challenge


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_stack", "completed")
    list_filter = ("completed", "stack")
    search_fields = ("title", "description")
    ordering = ("id",)
    readonly_fields = ("formatted_snippet",)

    def get_stack(self, obj):
        return ", ".join(obj.stack)

    get_stack.short_description = "Tech Stack"

    def formatted_snippet(self, obj):
        code = highlight(
            obj.snippet,
            JsxLexer(),
            HtmlFormatter(
                style='monokai',
                noclasses=True,
                nobackground=True,
                linenos=False,
            )
        )
        return mark_safe(
            f'<div style="background-color: #0f1115; padding: 15px; '
            f'border-radius: 4px; font-family: monospace;">{code}</div>'
        )

    formatted_snippet.short_description = "Code Snippet"

    fieldsets = (
        (None, {"fields": ("title", "description")}),
        (
            "Challenge Details",
            {
                "fields": ("stack", "formatted_snippet", "snippet"),
                "classes": ("collapse",),
            },
        ),
        ("Status", {"fields": ("completed",)}),
    )
