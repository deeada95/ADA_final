from django.contrib.auth.mixins import UserPassesTestMixin
from produs.models import Favorite


class UserIsReviewOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        review = Favorite.objects.get(pk=self.kwargs['pk'])
        if self.request.user == review.user:
            return True

        return False