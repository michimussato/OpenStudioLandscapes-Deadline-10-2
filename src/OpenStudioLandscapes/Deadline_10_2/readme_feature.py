import textwrap
import snakemd


def readme_feature(
        doc: snakemd.Document
) -> snakemd.Document:

    ## Some Specific information

    doc.add_heading(
        text="Get Deadline",
        level=1,
    )

    doc.add_paragraph(
        snakemd.Inline(
            text=textwrap.dedent(
                """
                The Deadline Installers are not part of the `OpenStudioLandscapes-Deadline` Feature.
                You will have to download the installers manually before you can use this Feature.
                """
            ),
            image={
                "Deadline": "https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/_static/Product_Button_Deadline.png",
                "test": "https://www.snakemd.io/en/latest/_static/icon.png"
            }["Deadline"],
            link="https://docs.thinkboxsoftware.com/products/deadline/10.2/1_User%20Manual/index.html",
        ).__str__()
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

    doc.add_paragraph(
        text=textwrap.dedent(
            """
            Deadline is free, however (legally), an AWS account is required to access the download area. 
            Also, the account is required to use all Deadline features. Register here:
            """
        )
    )

    doc.add_unordered_list(
        [
            "[https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup)",
        ]
    )

    doc.add_paragraph(
        text=textwrap.dedent(
            """
            Once logged in, you can download the Deadline tar archive from this website:
            """
        )
    )

    doc.add_unordered_list(
        [
            "[https://us-east-1.console.aws.amazon.com/deadlinecloud/home#/thinkbox](https://us-east-1.console.aws.amazon.com/deadlinecloud/home#/thinkbox)",
        ]
    )

    doc.add_paragraph(
        text=textwrap.dedent(
            """
            If you prefer to just download Deadline and use it without any AWS Cloud features, 
            here you can get the `tar` archive and the `sha256` directly:
            """
        )
    )

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

    doc.add_paragraph(
        text=textwrap.dedent(
            """
            Extract all contents for the `tar` archive to `OpenStudioLandscapes-Deadline-10-2/.payload/bin`.
            """
        )
    )

    doc.add_code(
        textwrap.dedent(
            """
            $ tree .payload
            .payload
            ├── bin
            │   ├── AWSPortalLink-1.2.1.0-linux-x64-installer.run
            │   ├── AWSPortalLink-1.2.1.0-linux-x64-installer.run.sig
            │   ├── DeadlineClient-10.2.1.1-linux-x64-installer.run
            │   ├── DeadlineClient-10.2.1.1-linux-x64-installer.run.sig
            │   ├── DeadlineRepository-10.2.1.1-linux-x64-installer.run
            │   └── DeadlineRepository-10.2.1.1-linux-x64-installer.run.sig
            ├── config
            └── data
            
            4 directories, 6 files
            """
        ),
        lang="shell",
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

    return doc


if __name__ == '__main__':
    pass
