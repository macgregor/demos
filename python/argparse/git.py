import argparse

def git_add(args):
    print 'adding file to git...'
    print 'parsed_args.filename = \'%s\'' % args.filename
    print 'parsed_args.debug = \'%s\'' % args.debug

def git_commit(args):
    print 'commiting to git...'
    print 'parsed_args.message = \'%s\'' % args.message
    print 'parsed_args.debug = \'%s\'' % args.debug

git_parser = argparse.ArgumentParser(prog='git', description='python demo for argpase - subparsers usage')

#configure the root parser object to process subcommands
git_subparsers = git_parser.add_subparsers()

#create a parent parser to inherit arguments from
parent = argparse.ArgumentParser(add_help=False)
parent.add_argument('-d', '--debug', action='store_true', default=False, help='enable debug logging')

#create a subparser to handle arguments when 'git add' is called
#the title of the subparser with the argument used as the command when using the cli
#pass in the parent parser with the debug flag using the 'parents' keyword, note it takes
#a list
git_file_add_parser = git_subparsers.add_parser('add', description='Add file contents to the index', parents=[parent])
git_file_add_parser.add_argument('filename', help='filename to add to index')

#this is a trick to have a function called by the parser which is matched
#so if git add ... is called the git_add() method will be called with the parsed args
#and it git commit ... is called the git_commit method will be called
git_file_add_parser.set_defaults(func=git_add)

#create a subparser to handle arguments when 'git commit' is called
git_commit_parser = git_subparsers.add_parser('commit', description='Record changes to the repository', parents=[parent])
git_commit_parser.add_argument('-m', '--message', help='Use the given <msg> as the commit message')

#another example of this can be found at https://docs.python.org/2.7/library/argparse.html#argparse.ArgumentParser.add_subparsers
git_commit_parser.set_defaults(func=git_commit)

args = git_parser.parse_args()

#call the function matched by subparsers
args.func(args)
