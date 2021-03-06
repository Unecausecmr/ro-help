# Generated by Django 3.0.4 on 2020-03-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0010_auto_20200317_1848"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ngo",
            name="county",
            field=models.CharField(
                choices=[
                    ("ALBA", "ALBA"),
                    ("ARGES", "ARGES"),
                    ("ARAD", "ARAD"),
                    ("BACAU", "BACAU"),
                    ("BIHOR", "BIHOR"),
                    ("BISTRITA-NASAUD", "BISTRITA-NASAUD"),
                    ("BRAILA", "BRAILA"),
                    ("BRASOV", "BRASOV"),
                    ("BOTOSANI", "BOTOSANI"),
                    ("BUZAU", "BUZAU"),
                    ("CLUJ", "CLUJ"),
                    ("CALARASI", "CALARASI"),
                    ("CARAS-SEVERIN", "CARAS-SEVERIN"),
                    ("CONSTANTA", "CONSTANTA"),
                    ("COVASNA", "COVASNA"),
                    ("DAMBOVITA", "DAMBOVITA"),
                    ("DOLJ", "DOLJ"),
                    ("GORJ", "GORJ"),
                    ("GALATI", "GALATI"),
                    ("GIURGIU", "GIURGIU"),
                    ("HUNEDOARA", "HUNEDOARA"),
                    ("HARGHITA", "HARGHITA"),
                    ("IALOMITA", "IALOMITA"),
                    ("IASI", "IASI"),
                    ("MEHEDINTI", "MEHEDINTI"),
                    ("MARAMURES", "MARAMURES"),
                    ("MURES", "MURES"),
                    ("NEAMT", "NEAMT"),
                    ("OLT", "OLT"),
                    ("PRAHOVA", "PRAHOVA"),
                    ("SIBIU", "SIBIU"),
                    ("SALAJ", "SALAJ"),
                    ("SATU-MARE", "SATU-MARE"),
                    ("SUCEAVA", "SUCEAVA"),
                    ("TULCEA", "TULCEA"),
                    ("TIMIS", "TIMIS"),
                    ("TELEORMAN", "TELEORMAN"),
                    ("VALCEA", "VALCEA"),
                    ("VRANCEA", "VRANCEA"),
                    ("VASLUI", "VASLUI"),
                    ("ILFOV", "ILFOV"),
                    ("BUCURESTI", "BUCURESTI"),
                    ("SECTOR 1", "SECTOR 1"),
                    ("SECTOR 2", "SECTOR 2"),
                    ("SECTOR 3", "SECTOR 3"),
                    ("SECTOR 4", "SECTOR 4"),
                    ("SECTOR 5", "SECTOR 5"),
                    ("SECTOR 6", "SECTOR 6"),
                ],
                max_length=50,
                verbose_name="County",
            ),
        ),
        migrations.AlterField(
            model_name="personalrequest",
            name="county",
            field=models.CharField(
                choices=[
                    ("ALBA", "ALBA"),
                    ("ARGES", "ARGES"),
                    ("ARAD", "ARAD"),
                    ("BACAU", "BACAU"),
                    ("BIHOR", "BIHOR"),
                    ("BISTRITA-NASAUD", "BISTRITA-NASAUD"),
                    ("BRAILA", "BRAILA"),
                    ("BRASOV", "BRASOV"),
                    ("BOTOSANI", "BOTOSANI"),
                    ("BUZAU", "BUZAU"),
                    ("CLUJ", "CLUJ"),
                    ("CALARASI", "CALARASI"),
                    ("CARAS-SEVERIN", "CARAS-SEVERIN"),
                    ("CONSTANTA", "CONSTANTA"),
                    ("COVASNA", "COVASNA"),
                    ("DAMBOVITA", "DAMBOVITA"),
                    ("DOLJ", "DOLJ"),
                    ("GORJ", "GORJ"),
                    ("GALATI", "GALATI"),
                    ("GIURGIU", "GIURGIU"),
                    ("HUNEDOARA", "HUNEDOARA"),
                    ("HARGHITA", "HARGHITA"),
                    ("IALOMITA", "IALOMITA"),
                    ("IASI", "IASI"),
                    ("MEHEDINTI", "MEHEDINTI"),
                    ("MARAMURES", "MARAMURES"),
                    ("MURES", "MURES"),
                    ("NEAMT", "NEAMT"),
                    ("OLT", "OLT"),
                    ("PRAHOVA", "PRAHOVA"),
                    ("SIBIU", "SIBIU"),
                    ("SALAJ", "SALAJ"),
                    ("SATU-MARE", "SATU-MARE"),
                    ("SUCEAVA", "SUCEAVA"),
                    ("TULCEA", "TULCEA"),
                    ("TIMIS", "TIMIS"),
                    ("TELEORMAN", "TELEORMAN"),
                    ("VALCEA", "VALCEA"),
                    ("VRANCEA", "VRANCEA"),
                    ("VASLUI", "VASLUI"),
                    ("ILFOV", "ILFOV"),
                    ("BUCURESTI", "BUCURESTI"),
                    ("SECTOR 1", "SECTOR 1"),
                    ("SECTOR 2", "SECTOR 2"),
                    ("SECTOR 3", "SECTOR 3"),
                    ("SECTOR 4", "SECTOR 4"),
                    ("SECTOR 5", "SECTOR 5"),
                    ("SECTOR 6", "SECTOR 6"),
                ],
                max_length=50,
                verbose_name="County",
            ),
        ),
    ]
