"""

Useful docs:
* https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser.add_argument
* https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser.parse_args
* https://docs.python.org/2/library/argparse.html#argparse.ArgumentParser.add_subparsers
"""
import argparse #this is all you need for basic argparse
import inspect, sys

def _all_functions():
    return [obj for name,obj in inspect.getmembers(sys.modules[__name__])
                     if (inspect.isfunction(obj) and name != '__main__' and not name.startswith('_'))]

def basic(args):
    print '='*80
    parser = argparse.ArgumentParser(description='python demo for argpase - basic usage')
    parser.add_argument('one')
    parser.add_argument('two', help='second argument')
    parser.add_argument('three', type=int, help='this one is an integer')
    parser.print_help()

    print '='*80
    print "Example: python demo.py first second 3\n"
    args = ['first', 'second', '3']
    parsed_args = parser.parse_args(args)

    print 'parsed_args.one = %s(\'%s\')' % (type(parsed_args.one).__name__, parsed_args.one)
    print 'parsed_args.two = %s(\'%s\')' % (type(parsed_args.two).__name__, parsed_args.two)
    print 'parsed_args.three = %s(%d)' % (type(parsed_args.three).__name__, parsed_args.three)
    print '='*80

def optionals(args):
    print '='*80
    parser = argparse.ArgumentParser(description='python demo for argpase - optionals usage')
    parser.add_argument('-a', help='short form')
    parser.add_argument('--bravo', help='long form')
    parser.add_argument('-c', '--charlie', help='short and long form together')
    parser.add_argument('-e', '--echo', dest='echo_echo_echo', help='alternate destination')
    parser.print_help()

    print '='*80
    print "Example: python demo.py -a optional_a --bravo optional_bravo -c optional_c_charlie --echo optional_echo_echo_echo\n"
    args = ['-a', 'optional_a', '--bravo', 'optional_bravo', '-c', 'optional_c_charlie', '--echo', 'optional_echo_echo_echo']
    parsed_args = parser.parse_args(args)

    print 'parsed_args.a = %s(\'%s\')' % (type(parsed_args.a).__name__, parsed_args.a)
    print 'parsed_args.bravo = %s(\'%s\')' % (type(parsed_args.bravo).__name__, parsed_args.bravo)

    #note: if you specify both long and short forms, the dest will be the long form not the short form.
    print 'parsed_args.charlie = %s(\'%s\') ' % (type(parsed_args.charlie).__name__, parsed_args.charlie)

    #note: we overrode the dest so instead of parsed_args.echo we use parsed_args.echo_echo_echo
    print 'parsed_args.echo_echo_echo = %s(\'%s\')' % (type(parsed_args.echo_echo_echo).__name__, parsed_args.echo_echo_echo)
    print '='*80

def defaults(args):
    print '='*80
    parser = argparse.ArgumentParser(description='python demo for argpase - defaults usage')
    parser.add_argument('--no-default', help='optional without a default')
    parser.add_argument('--default', help='optional with a default', default='this is the default value')
    parser.print_help()

    print '='*80
    print "Example: python demo.py\n"
    args = []
    parsed_args = parser.parse_args(args)

    #note: argparse replaces the '-' with a '_' in the default destination variable name
    print 'parsed_args.no_default = %s(%s)' % (type(parsed_args.no_default).__name__, parsed_args.no_default)
    print 'parsed_args.default = %s(\'%s\')' % (type(parsed_args.default).__name__, parsed_args.default)
    print '='*80

def flags(args):
    print '='*80
    parser = argparse.ArgumentParser(description='python demo for argpase - flags usage')
    parser.add_argument('-f', '--flag', help='this is a flag without arguments', action='store_true')
    parser.add_argument('--false-flag', help='this is a false flag', action='store_false')
    parser.add_argument('--default-flag', help='this is a flag with a default value', action='store_true', default=False)
    parser.print_help()

    print '='*80
    print "Example: python demo.py --flag --false-flag\n"
    args = ['--flag', '--false-flag']
    parsed_args = parser.parse_args(args)

    #note: argparse replaces the '-' with a '_' in the default destination variable name
    print 'parsed_args.flag = %s(%s)' % (type(parsed_args.flag).__name__, parsed_args.flag)
    print 'parsed_args.false_flag = %s(%s)' % (type(parsed_args.false_flag).__name__, parsed_args.false_flag)
    print 'parsed_args.default_flag = %s(%s)' % (type(parsed_args.default_flag).__name__, parsed_args.default_flag)
    print '='*80

def lists(args):
    print '='*80
    parser = argparse.ArgumentParser(description='python demo for argpase - lists usage')
    parser.add_argument('list', help='this is required list of arguments', nargs='+')
    parser.add_argument('--optional-list-fixed', help='this is an optional list of 3 arguments', nargs=3)
    parser.add_argument('--optional-list-int', help='this is an optional list of ints', nargs='+', type=int)
    parser.print_help()

    print '='*80
    print "Example: python demo.py a b c d --optional-list-fixed one two three --optional-list-int 1 2 3 4 5 6\n"
    args = ['a', 'b', 'c', 'd', '--optional-list-fixed', 'one', 'two', 'three', '--optional-list-int', '1', '2', '3', '4', '5', '6']
    print "Example: python demo.py %s\n" % ' '.join(args)
    parsed_args = parser.parse_args(args)

    print 'parsed_args.list = %s(\'%s\')' % (type(parsed_args.list).__name__, "\',\'".join(parsed_args.list))
    print 'parsed_args.optional_list_fixed = %s(\'%s\')' % (type(parsed_args.optional_list_fixed).__name__, "\',\'".join(parsed_args.optional_list_fixed))
    print 'parsed_args.optional_list_int = %s(%s)' % (type(parsed_args.optional_list_int).__name__, ','.join([str(i) for i in parsed_args.optional_list_int]))
    print '='*80

def subparser(args):
    print '='*80
    git_parser = argparse.ArgumentParser(prog='git', description='python demo for argpase - subparsers usage')
    git_parser.add_argument('--global-option', help='all subcommands can use this argument')

    #configure the root parser object to process subcommands
    git_subparsers = git_parser.add_subparsers()

    #create a subparser to handle arguments when 'git add' is called
    git_file_add_parser = git_subparsers.add_parser('add', description='Add file contents to the index')
    git_file_add_parser.add_argument('filename', help='filename to add to index')

    #create a subparser to handle arguments when 'git commit' is called
    git_commit_parser = git_subparsers.add_parser('commit', description='Record changes to the repository')
    git_commit_parser.add_argument('-m', '--message', help='Use the given <msg> as the commit message')
    git_parser.print_help()

    print '='*80
    git_file_add_parser.print_help()
    args = ['add', 'demo.py', '--global-option', 'foo']
    print "Example: git %s\n" % ' '.join(args)
    parsed_args = git_parser.parse_args(args)

    print 'parsed_args.filename = %s(\'%s\')' % (type(parsed_args.filename).__name__, parsed_args.filename)
    print 'parsed_args.global_option = %s(\'%s\')' % (type(parsed_args.global_option).__name__, parsed_args.global_option)

    print '='*80
    git_commit_parser.print_help()
    args = ['commit', '-m', 'my commit message', '--global-option', 'foo']
    print "Example: git %s\n" % ' '.join(args)
    parsed_args = git_parser.parse_args(args)

    print 'parsed_args.message = %s(\'%s\')' % (type(parsed_args.message).__name__, parsed_args.message)
    print 'parsed_args.global_option = %s(\'%s\')' % (type(parsed_args.global_option).__name__, parsed_args.global_option)
    print '='*80

def inherit(args):
    print '='*80
    git_parser = argparse.ArgumentParser(prog='git', description='python demo for argpase - subparsers usage, inherit args')

    #configure the root parser object to process subcommands
    git_subparsers = git_parser.add_subparsers()

    #create a parent parser to inherit arguments from
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument('-d', '--debug', action='store_true', default=False, help='enable debug logging')

    #create a subparser to handle arguments when 'git add' is called, inherit the --debug flag from parent parser
    git_file_add_parser = git_subparsers.add_parser('add', description='Add file contents to the index', parents=[parent])
    git_file_add_parser.add_argument('filename', help='filename to add to index')

    git_parser.print_help()

    print '='*80
    git_file_add_parser.print_help()
    args = ['add', 'demo.py', '--debug']
    print "Example: git %s\n" % ' '.join(args)
    parsed_args = git_parser.parse_args(args)

    print 'parsed_args.filename = %s(\'%s\')' % (type(parsed_args.filename).__name__, parsed_args.filename)
    print 'parsed_args.debug = %s(\'%s\')' % (type(parsed_args.debug).__name__, parsed_args.debug)

    print '='*80

def all(args):
    for f in _all_functions():
        if f.__name__ != 'all':
            f(args)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='argparse demo')
    subparsers = parser.add_subparsers()

    for f in _all_functions():
        subparsers.add_parser(f.__name__).set_defaults(func=f)

    args = parser.parse_args()
    args.func(args)
