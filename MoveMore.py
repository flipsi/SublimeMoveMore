import sublime, sublime_plugin

class MoveMoreCommand(sublime_plugin.TextCommand):
    def run(self, edit, amount=1):

        if (amount < 0):
            amount = -amount
            forward = False
        else:
            forward = True

        for i in range(amount):
            self.view.run_command('move', {'by': 'lines', 'forward': forward })
