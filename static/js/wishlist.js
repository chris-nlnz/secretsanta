$(function () {

    /**
     * On clicking a Group link, show group information in middle panel.
     */
    $(document).on('click', "a.group-link", function () {
        var url = $(this).data('url');

        // go back to group details tab when a new group is clicked
        $("a#home-tab").click();

        $("#group-panel").collapse('show');

        $("#group-panel .card-header").html(
            $(this).data('title')
        );
    });
});