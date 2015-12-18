import sublime, sublime_plugin

class MoveMoreCommand(sublime_plugin.TextCommand):

    def run(self, edit, amount=1, forward=True):

        # negative amount means opposite direction
        if (amount < 0):
            amount = -amount
            forward = not forward


        # extend if there is selected text
        # (there probably is a better implementation)
        extend = False
        for r in self.view.sel():
            if (r.size()):
                extend = True

        # and move!
        for i in range(amount):
            self.view.run_command('move', {
                'by': 'lines', 
                'forward': forward, 
                'extend': extend
            })



