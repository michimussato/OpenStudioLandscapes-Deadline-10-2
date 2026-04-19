import textwrap

import snakemd

# Todo
#  - [ ] expose RCS to web
#        - Pangolin Rule?
#          - What would be the the path to exclude? (i.e. /api/v3/*)
#        - Use SSL Certificate and fully disable Pangolin Protection?
#          - Resources:
#            - https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/remote-connection-server.html#remote-connection-server-ref-label
#            - https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/proxy-sslgen.html#ssl-cert-gen-ref-label


# REST API with examples
#
#
# [!TIP]
#
# If a documented query requires a JSON object that you do not
# know how to properly construct, it is often possible to do
# a GET query for the same object type and receive the JSON
# format that the query expects.
#
#
# - https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/rest-overview.html#
# - https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/index-rest-api.html
#   - https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/rest-jobs.html#get-all-the-jobs
#     - http://miniboss:8899/api/jobs
#   - https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/rest-jobs.html#get-job
#     - http://miniboss:8899/api/jobs?JobID=69de803adf6074790a6ca389
#   - https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/manual/rest-jobs.html#submit-job
#     - Todo
# curl
# - https://stackoverflow.com/a/36778045/2207196
# - https://stackoverflow.com/a/35095248/2207196
# - https://stackoverflow.com/a/69761368/2207196
# - https://stackoverflow.com/a/7173011/2207196
#   - curl --header "Content-Type: application/json" \
#     --request POST \
#     --data '{"username":"xyz","password":"xyz"}' \
#     http://localhost:3000/api/login
#   - curl --header "Content-Type: application/json" \
#     --request POST \
#     --data \
#       '{"JobInfo":"",\
#         "PluginInfo":"",
#         "AuxFiles":"",
#         "IdOnly":"",
#         }' \
#     http://miniboss:8899/api/jobs
#  curl --header "Content-Type: application/json" --request GET http://miniboss:8899/api/jobs | jq > /home/michael/git/repos/OpenStudioLandscapes/.features/OpenStudioLandscapes-Deadline-10-2/src/OpenStudioLandscapes/Deadline_10_2/doc/object.json


# curl --header "Content-Type: application/json" --request POST --data "{\"JobInfo\": \"{\\n  \\\"Plugin\\\": \\\"CommandLine\\\",\\n  \\\"Frames\\\": \\\"1197-1254x16,1197-1254x8,1197-1254x4,1197-1254x2,1197-1254x1\\\",\\n  \\\"Name\\\": \\\"Test Production - SH030 - 4_1201-1250_4 - Rendering - sh030_001.blend - 080 - blender\\\",\\n  \\\"Comment\\\": \\\"This is a new Bender job comment\\\",\\n  \\\"Department\\\": \\\"\\\",\\n  \\\"BatchName\\\": \\\"Batch: Test Production - SH030 - 4_1201-1250_4 - Rendering - sh030_001.blend - 080 - blender\\\",\\n  \\\"UserName\\\": \\\"root\\\",\\n  \\\"Pool\\\": null,\\n  \\\"SecondaryPool\\\": null,\\n  \\\"Group\\\": null,\\n  \\\"Priority\\\": 50,\\n  \\\"ChunkSize\\\": 1,\\n  \\\"ConcurrentTasks\\\": 1,\\n  \\\"LimitConcurrentTasksToNumberOfCpus\\\": true,\\n  \\\"OnJobComplete\\\": \\\"Nothing\\\",\\n  \\\"SynchronizeAllAuxiliaryFiles\\\": false,\\n  \\\"ForceReloadPlugin\\\": true,\\n  \\\"Sequential\\\": false,\\n  \\\"SuppressEvents\\\": false,\\n  \\\"Protected\\\": false,\\n  \\\"InitialStatus\\\": \\\"Active\\\",\\n  \\\"JobDependencies\\\": [],\\n  \\\"JobDependencyPercentage\\\": -1,\\n  \\\"IsFrameDependent\\\": false,\\n  \\\"FrameDependencyOffsetStart\\\": 0,\\n  \\\"FrameDependencyOffsetEnd\\\": 0,\\n  \\\"ResumeOnCompleteDependencies\\\": true,\\n  \\\"ResumeOnDeletedDependencies\\\": false,\\n  \\\"ResumeOnFailedDependencies\\\": false,\\n  \\\"RequiredAssets\\\": [],\\n  \\\"ScriptDependencies\\\": []\\n}\", \"PluginInfo\": \"{\\n  \\\"Executable\\\": \\\"/data/share/rez-packages/packages/blender/4.1.1/blender\\\",\\n  \\\"Arguments\\\": \\\"\\\\\\\"--enable-autoexec --background <QUOTE>\\\\\\\"/data/share/AWSPortalRoot1/fixtures/blender/sh030_001.blend\\\\\\\"<QUOTE> --render-output <QUOTE>\\\\\\\"/data/share/AWSPortalRoot1/out/Test Production/Shot/SH030/Rendering/080/raw/sh030_001.####.exr\\\\\\\"<QUOTE> --render-format EXR --engine CYCLES --frame-start <STARTFRAME> --frame-end <ENDFRAME> --threads 0 --render-anim -- --cycles-print-stats\\\\\\\"\\\"\\n}\", \"IdOnly\": false, \"AuxFiles\": []}" http://miniboss:8899/api/jobs


def readme_feature(
    doc: snakemd.Document,
    main_header: str,
) -> snakemd.Document:

    # Some Specific information

    doc.add_heading(
        text=main_header,
        level=1,
    )

    doc.add_paragraph(
        snakemd.Inline(
            text=textwrap.dedent("""\
                The Deadline Installers are not part of the `OpenStudioLandscapes-Deadline` Feature.
                You will have to download the installers manually before you can use this Feature.\
                """),
            image={
                "Deadline": "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/_static/Product_Button_Deadline.png",
                "test": "https://www.snakemd.io/en/latest/_static/icon.png",
            }["Deadline"],
            link="https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html",
        ).__str__()
    )

    doc.add_quote(text=textwrap.dedent("""\
            [!IMPORTANT]
            
            Disclaimer:
            
            Deadline is in [**Maintenance Mode**](https://docs.thinkboxsoftware.com/products/deadline/10.4/1_User%20Manual/manual/maintenance-mode-faq.html).
            I try to avoid Deadline customization wherever possible (custom plugins and events for example).
            Instead, I want to lower the dependency to external (especially
            closed source) applications and migrate as many post-steps to
            free/open dependencies as possible (or dependencies I own - like
            [OpenStudioLandscapes-DagsterCodeLocation-ShotProcessor](https://github.com/michimussato/OpenStudioLandscapes-DagsterCodeLocation-ShotProcessor)).
            """))

    doc.add_heading(
        text="Get Deadline",
        level=2,
    )

    doc.add_unordered_list(
        [
            "https://aws.amazon.com/thinkbox-deadline",
            "https://aws.amazon.com/media-services/thinkbox/",
        ]
    )

    doc.add_heading(
        text="Get Deadline 10.2",
        level=3,
    )

    doc.add_paragraph(text=textwrap.dedent("""\
            Deadline is free, however, an AWS account is required to access the download area as well
            as to use all Deadline Cloud features. Register here:\
            """))

    doc.add_unordered_list(
        [
            "[https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup)",
        ]
    )

    doc.add_paragraph(text=textwrap.dedent("""\
            Once logged in, you can download the Deadline tar archive from this website:\
            """))

    doc.add_unordered_list(
        [
            "[https://us-east-1.console.aws.amazon.com/deadlinecloud/home#/thinkbox](https://us-east-1.console.aws.amazon.com/deadlinecloud/home#/thinkbox)",
        ]
    )

    doc.add_paragraph(text=textwrap.dedent("""\
            If you prefer to just download Deadline and use it without any AWS Cloud features,
            here you can get the `tar` archive and the `sha256` directly:\
            """))

    doc.add_unordered_list(
        [
            "[https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.tar](https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.tar)",
            "[https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.sha256](https://thinkbox-installers.s3.us-west-2.amazonaws.com/Releases/Deadline/10.2/5_10.2.1.1/Deadline-10.2.1.1-linux-installers.sha256)",
        ]
    )

    doc.add_heading(
        text="Instructions",
        level=3,
    )

    doc.add_paragraph(text=textwrap.dedent("""\
            Extract all contents for the `tar` archive to your local drive - 
            for example to `~/Downloads/Deadline_10_2_Installers`.\
            """))

    doc.add_code(
        textwrap.dedent("""\
            $ tree ~/Downloads/Deadline_10_2_Installers
            ├── AWSPortalLink-1.2.1.0-linux-x64-installer.run
            ├── AWSPortalLink-1.2.1.0-linux-x64-installer.run.sig
            ├── DeadlineClient-10.2.1.1-linux-x64-installer.run
            ├── DeadlineClient-10.2.1.1-linux-x64-installer.run.sig
            ├── DeadlineRepository-10.2.1.1-linux-x64-installer.run
            └── DeadlineRepository-10.2.1.1-linux-x64-installer.run.sig\
"""),
        lang="generic",
    )

    doc.add_paragraph(text=textwrap.dedent("""\
            Then, specify the full paths of the `*.run` files in the `config.yml` file
            (usually `~/.config/OpenStudioLandscapes/config-store/OpenStudioLandscapes-Deadline-10-2/config.yml`
            if not specified otherwise):\
            """))

    doc.add_code(
        textwrap.dedent("""\
            # deadline_10_2_installer_aws_portal_link: REQUIRED (CHANGE_ME)
            deadline_10_2_installer_aws_portal_link: "~/Downloads/Deadline_10_2_Installers/AWSPortalLink-1.2.1.0-linux-x64-installer.run"
            # deadline_10_2_installer_deadline_client: REQUIRED (CHANGE_ME)
            deadline_10_2_installer_deadline_client: "~/Downloads/Deadline_10_2_Installers/DeadlineClient-10.2.1.1-linux-x64-installer.run"
            # deadline_10_2_installer_deadline_repository: REQUIRED (CHANGE_ME)
            deadline_10_2_installer_deadline_repository: "~/Downloads/Deadline_10_2_Installers/DeadlineRepository-10.2.1.1-linux-x64-installer.run"\
"""),
        lang="yaml",
    )

    doc.add_paragraph(text=textwrap.dedent("""\
            After doing so, you can enable the **OpenStudioLandscapes-Deadline-10-2** and 
            **OpenStudioLandscapes-Deadline-10-2-Worker** Features in their `config.yml` files:\
            """))

    doc.add_code(
        textwrap.dedent("""\
            enabled: true\
"""),
        lang="yaml",
    )

    doc.add_heading(
        text="Documentation",
        level=2,
    )

    doc.add_heading(
        text="User Manual",
        level=3,
    )

    doc.add_unordered_list(
        [
            "[https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html](https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html)",
        ]
    )

    doc.add_heading(
        text="Scripting Reference",
        level=3,
    )

    doc.add_unordered_list(
        [
            "[https://docs.thinkboxsoftware.com/products/deadline/10.2/2_Scripting%20Reference/index.html](https://docs.thinkboxsoftware.com/products/deadline/10.2/2_Scripting%20Reference/index.html)",
        ]
    )

    doc.add_heading(
        text="Python Reference",
        level=3,
    )

    doc.add_unordered_list(
        [
            "[https://docs.thinkboxsoftware.com/products/deadline/10.2/3_Python%20Reference/index.html](https://docs.thinkboxsoftware.com/products/deadline/10.2/3_Python%20Reference/index.html)",
        ]
    )

    doc.add_heading(
        text="Information on Usage Based Licensing (UBL)",
        level=3,
    )

    doc.add_unordered_list(
        [
            "[https://marketplace.thinkboxsoftware.com](https://marketplace.thinkboxsoftware.com)",
            "[https://awsthinkbox.zendesk.com/hc/en-us/articles/22883209044759-AWS-Deadline-Cloud-UBL-for-Deadline-10-on-AWS](https://awsthinkbox.zendesk.com/hc/en-us/articles/22883209044759-AWS-Deadline-Cloud-UBL-for-Deadline-10-on-AWS)",
        ]
    )

    doc.add_heading(
        text="Known Issues",
        level=2,
    )

    doc.add_heading(
        text='Could not find the Qt platform plugin "wayland"',
        level=3,
    )

    doc.add_heading(
        text="Error Message",
        level=4,
    )

    doc.add_code(
        textwrap.dedent("""\
            # $ /opt/Thinkbox/Deadline10/bin/deadlinemonitor
            qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
            This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

            Available platform plugins are: linuxfb, minimal, offscreen, vnc, webgl, xcb.

            Aborted                    (core dumped) /opt/Thinkbox/Deadline10/bin/deadlinemonitor\
"""),
        lang="generic",
    )

    doc.add_heading(
        text="Solution",
        level=4,
    )

    doc.add_code(
        textwrap.dedent("""\
            export QT_QPA_PLATFORM=xcb\
"""),
        lang="shell",
    )

    doc.add_horizontal_rule()

    return doc


if __name__ == "__main__":
    pass
