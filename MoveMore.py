import sublime, sublime_plugin

class MoveMoreCommand(sublime_plugin.TextCommand):

    def run(self, edit, amount=1):

        if (amount < 0):
            amount = -amount
            forward = False
        else:
            forward = True


        # extend if there is selected text
        # (there probably is a better implementation)
        extend = False
        for r in self.view.sel():
            if (r.size()):
                extend = True

        for i in range(amount):
            self.view.run_command('move', {
                'by': 'lines', 
                'forward': forward, 
                'extend': extend
            })



