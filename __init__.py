# Answer Button Sounds addon
# Copyright (C) 2019-2020 Kyle "Khonkhortisan" Mills <https://github.com/khonkhortisan>
# Answer Button Sounds (original)
	# Ankiweb https://ankiweb.net/shared/info/679615590
	# github https://github.com/khonkhortisan/Answer-Button-Sounds
# Copyright (C) 2025 Shigeyuki <http://patreon.com/Shigeyuki>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os

from aqt import gui_hooks
from aqt.sound import play, clearAudioQueue, AVPlayer

addon_path = os.path.dirname(__file__)
user_files = os.path.join(addon_path, "user_files")

def answersound(reviewer, card, ease):
	if ease == 1:
		clearAudioQueue()
		play(os.path.join(user_files, "again.mp3"))
	if ease == 2:
		clearAudioQueue()
		play(os.path.join(user_files, "hard.mp3"))
	if ease == 3:
		clearAudioQueue()
		play(os.path.join(user_files, "good.mp3"))
	if ease == 4:
		clearAudioQueue()
		play(os.path.join(user_files, "easy.mp3"))


gui_hooks.reviewer_did_answer_card.append(answersound)

def _play_tags(self:AVPlayer, tags):
    """Clear the existing queue, then start playing provided tags."""
    self._enqueued = tags[:]
    #if self.interrupt_current_audio:
    #if self.interrupt_current_audio and not nextCard
    if self.interrupt_current_audio and False: #TODO: do clear audio when flipping to back, don't clear it when going to the next card. This was easier when it was in the nextCard function so I could just disable it there.
        self._stop_if_playing()
    self._play_next_if_idle()
AVPlayer.play_tags=_play_tags
