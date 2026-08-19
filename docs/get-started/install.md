# Install and enable UmbraScript

Add the UmbraScript package to an Umbraco CMS project, restart the website, and grant the appropriate user groups access to its backoffice section.

## Install the package

Open a terminal in the directory that contains your Umbraco `.csproj` file, then run:

```console
dotnet add package UmbraScript
```

Build and restart the website so Umbraco can discover the package:

```console
dotnet build
dotnet run
```

If your website is managed by another hosting process, use that process to rebuild and restart it instead.

## Grant section access

An administrator must grant access to the UmbraScript section through an Umbraco user group.

1. Sign in to the Umbraco backoffice as an administrator.
2. Open **Users**.
3. Open **User Groups** and select the group that should use UmbraScript.
4. Under **Assign access**, enable the UmbraScript section.
5. Save the user group.
6. Sign out and back in if the new section does not appear immediately.

Grant access only to people who understand the effect of the commands they will run. Read [Permissions and safe use](../administration/permissions-and-safety.md) before enabling a production user group.

## Verify the installation

Open the UmbraScript section in the backoffice. The console should be available for the signed-in user.

Continue with [Run your first command](first-command.md).

## Update UmbraScript

To install a specific package version, pass the version to the .NET CLI:

```console
dotnet add package UmbraScript --version <VERSION>
```

Rebuild and restart the website after changing the package version.
