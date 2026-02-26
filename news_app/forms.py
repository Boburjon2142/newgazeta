from pathlib import Path

from django import forms

from .models import Comment, Contact, News


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class BaseNewsForm(forms.ModelForm):
    video = forms.FileField(
        required=False,
        help_text="MP4, MOV, M4V, WEBM, OGV. Max: 600MB",
        widget=forms.ClearableFileInput(attrs={"accept": "video/*"}),
    )

    class Meta:
        model = News
        fields = (
            'title', 'title_uz', 'title_uz_cyrl',
            'author', 'author_uz', 'author_uz_cyrl',
            'slug',
            'body', 'body_uz', 'body_uz_cyrl',
            'image', 'category', 'status',
        )

    def clean_video(self):
        video = self.cleaned_data.get("video")
        if not video:
            return video

        allowed_ext = {".mp4", ".mov", ".m4v", ".webm", ".ogv"}
        ext = Path(video.name).suffix.lower()
        if ext not in allowed_ext:
            raise forms.ValidationError("Faqat MP4, MOV, M4V, WEBM, OGV formatlari ruxsat etiladi.")

        max_size = 600 * 1024 * 1024
        if video.size > max_size:
            raise forms.ValidationError("Video hajmi 600MB dan oshmasligi kerak.")

        return video


class NewsCreateForm(BaseNewsForm):
    pass


class NewsUpdateForm(BaseNewsForm):
    pass
